from datetime import datetime
from typing import Union, Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import CharityProject, Donation


async def invest_funds(
        session: AsyncSession,
        new_entity: Union[CharityProject, Donation]
) -> None:
    if isinstance(new_entity, CharityProject):
        await invest_for_entity(session, new_entity, Donation)
    elif isinstance(new_entity, Donation):
        await invest_for_entity(session, new_entity, CharityProject)

    await session.commit()
    await session.refresh(new_entity)


async def invest_for_entity(
        session: AsyncSession,
        entity: Union[CharityProject, Donation],
        other_entity: Union[Type[CharityProject], Type[Donation]]
) -> None:
    open_entities = await session.execute(
        select(other_entity).filter(
            other_entity.fully_invested.is_(False)
        )
    )
    open_entities = open_entities.scalars().all()

    for open_entity in open_entities:
        amount_to_invest = min(
            entity.full_amount - entity.invested_amount,
            open_entity.full_amount - open_entity.invested_amount
        )
        if amount_to_invest > 0:
            entity.invested_amount += amount_to_invest
            open_entity.invested_amount += amount_to_invest
            if entity.invested_amount == entity.full_amount:
                entity.fully_invested = True
                entity.close_date = datetime.now()

            if open_entity.invested_amount == open_entity.full_amount:
                open_entity.fully_invested = True
                open_entity.close_date = datetime.now()

            session.add(entity)
            session.add(open_entity)
