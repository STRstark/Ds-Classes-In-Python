import java.util.HashMap;
import java.util.Map;
class Contact {
    private String fullName;
    private String nickname;
    private String phoneNumber;
    private String email;
    private String jobInfo;

    public Contact(String fullName, String nickname, String phoneNumber, String email, String jobInfo) {
        this.fullName = fullName;
        this.nickname = nickname;
        this.phoneNumber = phoneNumber;
        this.email = email;
        this.jobInfo = jobInfo;
    }
    @Override
    public String toString() {
        return "Name: " + fullName + " (" + nickname + ")\n" +
               "Phone: " + phoneNumber + "\n" +
               "Email: " + email + "\n" +
               "Job: " + jobInfo + "\n";
    }
}
class TreeNode {
    Map<Character, TreeNode> children = new HashMap<>();
    boolean isEndOfNumber = false;
    Contact contact = null; // Use Contact object directly
}
class PhoneNumberTree {
    TreeNode root;

    public PhoneNumberTree() {
        root = new TreeNode();
        root.children.put('0', new TreeNode());
        root.children.get('0').children.put('9', new TreeNode());
    }
}
public class Main { // Example for usage
    public static void main(String[] args) {
        PhoneNumberTree phoneBook = new PhoneNumberTree();
        Contact contact1 = new Contact("John Doe", "JD", "1234567890", "john.doe@example.com", "Software Engineer");
        System.out.println(contact1);
    }
}

    