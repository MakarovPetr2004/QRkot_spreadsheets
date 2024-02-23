from datetime import datetime
from aiogoogle import Aiogoogle

from .constants import (
    SPREADSHEET_BODY, PERMISSIONS_BODY, UPDATE_BODY, TABLE_VALUES,
    FORMAT
)


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    date_time_now = datetime.now().strftime(FORMAT)

    spreadsheet_body = SPREADSHEET_BODY
    spreadsheet_body['properties']['title'] = f'Отчёт на {date_time_now}'
    service = await wrapper_services.discover('sheets', 'v4')

    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=SPREADSHEET_BODY)
    )
    spreadsheet_id = response['spreadsheetId']

    return spreadsheet_id


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover('drive', 'v3')

    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=PERMISSIONS_BODY,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheet_id: str,
        charity_projects: list,
        wrapper_services: Aiogoogle
) -> None:
    date_time_now = datetime.now().strftime(FORMAT)

    service = await wrapper_services.discover('sheets', 'v4')

    table_values = TABLE_VALUES
    table_values[0][1] = date_time_now

    for ch in charity_projects:
        new_ch = [
            str(ch['name']), str(ch['time_spent']), str(ch['description'])
        ]
        table_values.append(new_ch)

    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range='A1:E30',
            valueInputOption='USER_ENTERED',
            json=UPDATE_BODY
        )
    )
