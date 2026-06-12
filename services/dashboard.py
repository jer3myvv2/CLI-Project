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
        print("4. Edit User")
        print("5. Delete User")
        print("6. Edit Project")
        print("7. Delete Project")
        print("8. Exit")

        choice = input("Select an option (1-8): ")
        
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
            user_id = input("Enter user ID to edit: ").strip()
            name = input("Enter new user name (leave blank to keep current): ").strip()
            if not user_id:
                print("User ID is required.")
                continue
            updated = user_service.update_user(user_id, name or None)
            print("User updated successfully!" if updated else "User not found.")

        elif choice == '5':
            user_id = input("Enter user ID to delete: ").strip()
            if not user_id:
                print("User ID is required.")
                continue
            deleted = user_service.delete_user(user_id)
            print("User deleted successfully!" if deleted else "User not found.")

        elif choice == '6':
            project_id = input("Enter project ID to edit: ").strip()
            name = input("Enter new project name (leave blank to keep current): ").strip()
            description = input("Enter new project description (leave blank to keep current): ").strip()
            user_id = input("Enter new user ID (leave blank to keep current): ").strip()
            if not project_id:
                print("Project ID is required.")
                continue
            updated = project_service.update_project(project_id, name=name or None, description=description or None, user_id=user_id or None)
            print("Project updated successfully!" if updated else "Project not found.")

        elif choice == '7':
            project_id = input("Enter project ID to delete: ").strip()
            if not project_id:
                print("Project ID is required.")
                continue
            deleted = project_service.delete_project(project_id)
            print("Project deleted successfully!" if deleted else "Project not found.")

        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    run_dashboard()