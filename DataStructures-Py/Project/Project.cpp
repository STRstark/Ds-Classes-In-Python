#include <string>
#include <unordered_map>

class Contact {
public:
    Contact(const std::string& full_name, const std::string& nickname,
            const std::string& phone_number, const std::string& email,
            const std::string& job_info) :
        full_name(full_name), nickname(nickname), phone_number(phone_number),
        email(email), job_info(job_info) {}

    std::string to_string() const {
        return "Name: " + full_name + " (" + nickname + ")\n" +
               "Phone: " + phone_number + "\n" +
               "Email: " + email + "\n" +
               "Job: " + job_info + "\n";
    }
private:
    std::string full_name;
    std::string nickname;
    std::string phone_number;
    std::string email;
    std::string job_info;
};
class TreeNode {
public:
    TreeNode() : is_end_of_number(false), contact_name(nullptr) {}

    std::unordered_map<char, TreeNode*> children;
    bool is_end_of_number;
    std::string* contact_name; 
};
class PhoneNumberTree {
public:
    PhoneNumberTree() {
        root = new TreeNode(); 
        root->children['0'] = new TreeNode();
        root->children['0']->children['9'] = new TreeNode();
    }

    ~PhoneNumberTree() {
        //Destructor to clean up dynamically allocated memory (exercise) not needed
    }
private:
    TreeNode* root; 


