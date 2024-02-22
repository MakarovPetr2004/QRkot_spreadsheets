from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    @staticmethod
    async def get_project_id_by_name(
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    @staticmethod
    async def get_projects_by_completion_rate(session: AsyncSession):
        result = await session.execute(
            select(CharityProject).filter(
                CharityProject.fully_invested.is_(True)
            )
        )
        closed_projects = result.scalars().all()

        sorted_projects = sorted(
            closed_projects,
            key=lambda project: (
                project.close_date - project.create_date
            )
        )

        projects_list = []
        for project in sorted_projects:
            time_spent = project.close_date - project.create_date
            days = time_spent.days
            hours, remainder = divmod(time_spent.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            milliseconds = time_spent.microseconds // 1000
            formatted_time = f"{days} days {hours:02}:{minutes:02}:{seconds:02}.{milliseconds:06}"

            projects_list.append({
                'name': project.name,
                'time_spent': formatted_time,
                'description': project.description
            })

        return projects_list


charity_project_crud = CRUDCharityProject(CharityProject)
