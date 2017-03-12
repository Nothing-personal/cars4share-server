from mongoengine import Document, EmbeddedDocument, fields


class User(Document):
    name = fields.StringField(required=True, min_length=1, max_length=50)
    surname = fields.StringField(required=True, min_length=1, max_length=50)
    email = fields.EmailField(required=True)
    phone_number = fields.StringField(required=True)
    date_of_birth = fields.DateTimeField(required=True)
    sex = fields.StringField(required=True)
    is_verified = fields.BooleanField(default=False)
    passport = fields.StringField  # will store links on images/documents
    driver_license = fields.StringField
    credit_card = fields.EmbeddedDocument(CreditCard)  # need to think about should we store this data or not
    feedback = fields.ListField(fields.Document(Feedback))  # only user feedback will be here
    account_type = fields.StringField(required=True)


class CreditCard(EmbeddedDocument):
    card_number = fields.StringField(required=True)
    cardholder_name = fields.StringField(required=True)
    cvv_code = fields.StringField(required=True, max_length=3)
    due_date = fields.DateTimeField(required=True)


class Feedback(Document):
    message = fields.StringField
    rate = fields.IntField(min_value=1, max_value=5, required=True)
