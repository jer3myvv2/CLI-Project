from Models.Project import Project
from Models.users import users
from services.Project_service import ProjectService
from services.User_service import UserService


def run_dashboard():
    user_service = UserService()
    project_service = ProjectService()

    while True:
        print("\n--- Project Management CLI ---")
        print("1. Create User")
        print("2. Create Project")
        print("3. View Projects by User")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            user_id = input("Enter user ID: ").strip()
            name = input("Enter user name: ").strip()

            if not user_id or not name:
                print("User ID and name are required.")
                continue

            user_service.save_user(users(user_id, name))
            print("User created!")

        elif choice == '2':
            user_id = input("Enter user ID: ").strip()
            project_id = input("Enter project ID: ").strip()
            name = input("Enter project name: ").strip()
            description = input("Enter project description: ").strip()

            if not user_id or not project_id or not name:
                print("User ID, project ID, and project name are required.")
                continue

            project = Project(project_id, name, description, user_id)
            saved = project_service.save_project(project)
            print("Project saved successfully!" if saved else "Failed to save project.")

        elif choice == '3':
            user_id = input("Enter user ID to view projects: ").strip()
            projects = project_service.get_projects_by_user(user_id)

            if not projects:
                print("No projects found for that user.")
            else:
                print("\nProjects for user", user_id)
                for project in projects:
                    print(f"- {project['project_id']}: {project['name']} ({project['description']})")
            
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    run_dashboard()