class Contact:
    def __init__(self, full_name, nickname, phone_number, email, job_info):
        self.full_name = full_name
        self.nickname = nickname
        self.phone_number = phone_number
        self.email = email
        self.job_info = job_info

    def __str__(self):
        return f"Nmae: {self.full_name} ({self.nickname})\nPhone: {self.phone_number}\nEmail: {self.email}\nJob: {self.job_info}"

class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False
        self.contact_name = None
        
class PhoneNumberTree:
    def __init__(self):
        self.root = TreeNode()
        self.root.children['0'] = TreeNode()
        self.root.children['0'].children['9'] = TreeNode()

