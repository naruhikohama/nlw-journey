

class ActivityFinder:
    def __init__(self, activities_repository):
        self.__activities_repository = activities_repository

    def find_from_trip(self, trip_id: str) -> dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(trip_id)

            activities_infos = []
            for activity in activities:
                activity_info = {
                    "id": activity[0],
                    "title": activity[2],
                    "occurs_at": activity[3]
                }
                activities_infos.append(activity_info)

            return {
                "body": activities_infos,
                "status_code": 200
            }
        
        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400
            }