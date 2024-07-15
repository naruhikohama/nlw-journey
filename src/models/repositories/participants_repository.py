from sqlite3 import Connection

class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_participant(self, participant_infos) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO participants (id, trip_id, emails_to_invite_id, name) 
            VALUES (?, ?, ?, ?)
            """,
            (participant_infos["id"],
            participant_infos["trip_id"],
            participant_infos["emails_to_invite_id"],
            participant_infos["name"],)
        )
        self.__conn.commit()

    def find_participants_from_trip(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT 
                p.id, 
                p.name,
                p.is_confirmed,
                e.email
            FROM participants p
            JOIN emails_to_invite e ON p.emails_to_invite_id = e.id
            WHERE p.trip_id = ?
            """,
            (trip_id,)
        )
        return cursor.fetchall()
    
    def update_participant_status(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            UPDATE participants
            SET is_confirmed = 1
            WHERE id = ?
            """,
            (participant_id,)
        )
        self.__conn.commit()

        