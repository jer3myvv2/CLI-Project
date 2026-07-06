try:
    from rich.console import Console
    from rich.panel import Panel
    HAVE_RICH = True
except ModuleNotFoundError:
    Console = None
    Panel = None
    HAVE_RICH = False

from Models.Project import Project
from Models.users import users
from services.Project_service import ProjectService
from services.User_service import UserService


console = Console() if HAVE_RICH else None


def print_message(text, style=None):
    if console:
        if style:
            console.print(f"[{style}]{text}[/{style}]")
        else:
            console.print(text)
    else:
        print(text)


def run_dashboard():
    user_service = UserService()
    project_service = ProjectService()

    while True:
        if HAVE_RICH and Panel:
            console.print(Panel.fit("[bold cyan]Project Management CLI[/bold cyan]", border_style="blue"))
        else:
            print("\n--- Project Management CLI ---")

        print_message("1. Create User", "green")
        print_message("2. Create Project", "green")
        print_message("3. View Projects by User", "green")
        print_message("4. List All Users", "green")
        print_message("5. List All Projects", "green")
        print_message("6. Edit User", "green")
        print_message("7. Delete User", "green")
        print_message("8. Edit Project", "green")
        print_message("9. Delete Project", "green")
        print_message("10. Exit", "green")

        choice = input("Select an option (1-10): ")
        
        if choice == '1':
            user_id = input("Enter user ID: ").strip()
            name = input("Enter user name: ").strip()

            if not user_id or not name:
                print_message("User ID and name are required.", "red")
                continue

            user_service.save_user(users(user_id, name))
            print_message("User created!", "bold green")

        elif choice == '2':
            user_id = input("Enter user ID: ").strip()
            project_id = input("Enter project ID: ").strip()
            name = input("Enter project name: ").strip()
            description = input("Enter project description: ").strip()

            if not user_id or not project_id or not name:
                print_message("User ID, project ID, and project name are required.", "red")
                continue

            project = Project(project_id, name, description, user_id)
            saved = project_service.save_project(project)
            print_message("Project saved successfully!" if saved else "Failed to save project.", "bold green" if saved else "red")

        elif choice == '3':
            user_id = input("Enter user ID to view projects: ").strip()
            projects = project_service.get_projects_by_user(user_id)

            if not projects:
                print_message("No projects found for that user.", "yellow")
            else:
                print_message(f"\nProjects for user {user_id}", "bold cyan")
                for project in projects:
                    print_message(f"- {project['project_id']}: {project['name']} ({project['description']})", "magenta")
            
        elif choice == '4':
            users_list = user_service.get_all_users()
            if not users_list:
                print_message("No users found.", "yellow")
            else:
                print_message("\nAll users:", "bold cyan")
                for user in users_list:
                    print_message(f"- {user.get('user_id', 'N/A')}: {user.get('name', 'N/A')}", "magenta")

        elif choice == '5':
            projects_list = project_service.get_all_projects()
            if not projects_list:
                print_message("No projects found.", "yellow")
            else:
                print_message("\nAll projects:", "bold cyan")
                for project in projects_list:
                    print_message(f"- {project.get('project_id', 'N/A')}: {project.get('name', 'N/A')} ({project.get('description', 'N/A')})", "magenta")

        elif choice == '6':
            user_id = input("Enter user ID to edit: ").strip()
            name = input("Enter new user name (leave blank to keep current): ").strip()
            if not user_id:
                print_message("User ID is required.", "red")
                continue
            updated = user_service.update_user(user_id, name or None)
            print_message("User updated successfully!" if updated else "User not found.", "bold green" if updated else "red")

        elif choice == '7':
            user_id = input("Enter user ID to delete: ").strip()
            if not user_id:
                print_message("User ID is required.", "red")
                continue
            deleted = user_service.delete_user(user_id)
            print_message("User deleted successfully!" if deleted else "User not found.", "bold green" if deleted else "red")

        elif choice == '8':
            project_id = input("Enter project ID to edit: ").strip()
            name = input("Enter new project name (leave blank to keep current): ").strip()
            description = input("Enter new project description (leave blank to keep current): ").strip()
            user_id = input("Enter new user ID (leave blank to keep current): ").strip()
            if not project_id:
                print_message("Project ID is required.", "red")
                continue
            updated = project_service.update_project(project_id, name=name or None, description=description or None, user_id=user_id or None)
            print_message("Project updated successfully!" if updated else "Project not found.", "bold green" if updated else "red")

        elif choice == '9':
            project_id = input("Enter project ID to delete: ").strip()
            if not project_id:
                print_message("Project ID is required.", "red")
                continue
            deleted = project_service.delete_project(project_id)
            print_message("Project deleted successfully!" if deleted else "Project not found.", "bold green" if deleted else "red")

        elif choice == '10':
            print_message("Exiting...", "yellow")
            break
        else:
            print_message("Invalid choice, please try again.", "red")

if __name__ == "__main__":
    run_dashboard()