import datetime

from project.main import db
from project.main.model.project import Project
from project.main.model.project_user import ProjectUser


def save_new_project(data, current_user_email):
    project = Project.query.filter_by(name=data['name']).first()
    if not project:
        new_project = Project(
            name=data['name'],
            created_date=datetime.datetime.utcnow()
        )
        save_changes(new_project, current_user_email)
        response_object = {
            'status': 'success',
            'message': 'Successfully added.',
            'project_id': new_project.id
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Project name already exists. Please change the name.',
        }
        return response_object, 409


def get_user_projects(current_user_email):
    return Project.query.join(ProjectUser).filter_by(user_email=current_user_email).all()


def get_project(project_id):
    return Project.query.filter_by(id=project_id).first()


def save_changes(project_data, current_user_email):
    db.session.add(project_data)
    db.session.flush()
    db.session.commit()

    project_user = ProjectUser(
        user_email=current_user_email,
        project_id=project_data.id,
        project_owner=True
    )

    db.session.add(project_user)
    db.session.flush()
    db.session.commit()


def delete_project(project_id):
    project = Project.query.filter_by(id=project_id).first()
    if project:
        delete_project_from_db(project)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.'
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': "No project found!",
        }
        return response_object, 404


def delete_project_from_db(project):
    db.session.delete(project)
    db.session.commit()
