import java.util.*;

public class TaskTracker {
    static class Task {
        String description;
        boolean done;

        Task(String description) {
            this.description = description;
            this.done = false;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Task> tasks = new ArrayList<>();

        while(true) {
            System.out.println("Commands: add, list, done, exit");
            String command = scanner.nextLine();

            switch(command) {
                case "add":
                    System.out.print("Task description: ");
                    String desc = scanner.nextLine();
                    tasks.add(new Task(desc));
                    break;
                case "list":
                    for(int i=0; i<tasks.size(); i++) {
                        Task t = tasks.get(i);
                        System.out.println((i+1) + ". [" + (t.done ? "x" : " ") + "] " + t.description);
                    }
                    break;
                case "done":
                    System.out.print("Task number to mark done: ");
                    int num = scanner.nextInt();scanner.nextLine();
                    if(num > 0 && num <= tasks.size()) tasks.get(num-1).done = true;
                    break;
                case "exit":
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Unknown command.");
            }
        }
    }
}
