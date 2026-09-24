def calculate_average_age(users):
    """Calculate the average numeric age from a list of user dictionaries. """
    valid_ages = []
    
    for user in users:
        age = user.get("age")
        if isinstance(age, (int, float)) and not isinstance(age, bool):
            valid_ages.append(age)
            
    if not valid_ages:
        return 0.0
        
    return sum(valid_ages) / len(valid_ages)


def get_active_user_emails(users):
    """Return a list of email addresses for users who are marked active."""
   
    emails = []
    
    for user in users:
        if user.get("is_active") and "email" in user:
            emails.append(user["email"])
            
    return emails