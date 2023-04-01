from config import database
from model import ReportType


class ReportAPI:
    @staticmethod
    async def get_report_all(report_type: ReportType):
        reports = []
        collection = database.get_collection(report_type).find()
        async for report in collection:
            reports.append(report)
        return reports

    @staticmethod
    async def get_report_code(report_type: ReportType, stock_code: str):
        return await database[report_type].find_one({"stock_code": stock_code})
