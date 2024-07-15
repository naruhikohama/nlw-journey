import uuid

class ParticipantCreator:
    def __init__(self, participants_repository, emails_repository) -> None:
        self.__participants_repository = participants_repository
        self.__emails_repository = emails_repository

    def create(self, body, trip_id) -> dict:
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            emails_infos = {
                "email": body["email"],
                "id": email_id,
                "trip_id": trip_id
            }


            participant_infos = {
                "name": body["name"],
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id
            }

            self.__emails_repository.registry_email(emails_infos)
            self.__participants_repository.registry_participant(participant_infos)

            return {
                "body": {"participant_id": participant_id},
                "status_code": 201
            }

        except Exception as e:
            return {
                "body": {"error": "Bad Request", "message": str(e)},
                "status_code": 400
           }