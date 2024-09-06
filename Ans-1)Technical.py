# Data structure for participants and projects
participants = []  # list of participants with their skill levels
projects = []  # list of projects with required skill levels for roles

# Function to assign participants to projects
def assign_participants_to_projects(participants, projects):
    completed_projects = 0

    for project in projects:
        assigned_roles = {}
        for role, required_level in enumerate(project.roles):
            for participant in participants:
                if participant.skills[role] >= required_level:
                    assigned_roles[role] = participant
                elif participant.skills[role] == required_level - 1:
                    mentor_found = False
                    for mentor_role, mentor in assigned_roles.items():
                        if mentor.skills[role] > required_level:
                            mentor_found = True
                            assigned_roles[role] = participant
                            break
                    if mentor_found:
                        break
        
        # Check if all roles are filled
        if len(assigned_roles) == len(project.roles):
            completed_projects += 1
    
    return completed_projects

# Example usage
completed_projects_count = assign_participants_to_projects(participants, projects)
print(completed_projects_count)
