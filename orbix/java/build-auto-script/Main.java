import java.util.Scanner;

public class BuildScriptGenerator {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter groupId: ");
        String groupId = in.nextLine();
        System.out.print("Enter artifactId: ");
        String artifactId = in.nextLine();

        String pom = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
            + "<project xmlns=\"http://maven.apache.org/POM/4.0.0\"\n"
            + "  xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n"
            + "  xsi:schemaLocation=\"http://maven.apache.org/POM/4.0.0\n"
            + "  http://maven.apache.org/xsd/maven-4.0.0.xsd\">\n"
            + "  <modelVersion>4.0.0</modelVersion>\n"
            + "  <groupId>" + groupId + "</groupId>\n"
            + "  <artifactId>" + artifactId + "</artifactId>\n"
            + "  <version>1.0-SNAPSHOT</version>\n"
            + "</project>\n";

        System.out.println("Generated pom.xml:\n" + pom);
        in.close();
    }
}
