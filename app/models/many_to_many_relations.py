from database import db

event_to_user_info = db.Table(
    "event_to_user_info",
    db.metadata,
    db.Column("event_id", db.ForeignKey("event.id")),
    db.Column("user_info_id", db.ForeignKey("user_info.id")),
)

event_to_field = db.Table(
    "event_to_field",
    db.metadata,
    db.Column("event_id", db.ForeignKey("event.id")),
    db.Column("field_id", db.ForeignKey("field.id"))
)

__all__ = [
    "event_to_user_info",
    "event_to_field"
]