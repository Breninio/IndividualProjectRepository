/*export class Project {
  project_id: number;
  project_name: string;
  project_manager: string;

  constructor(project_id, project_name, project_manager){
    this.project_id = project_id;
    this.project_name = project_name;
    this.project_manager = project_manager;
  }
}*/
export interface Activities {
  activity_id: number;
  activity_title: string;
  activity_description: string;
  activity_startDate: Date;
  activity_endDate: Date;
  activity_reason: string;
  activity_learnings: string;
  activity_application: string;
  activity_support: string;
  activity_participant1: string;
  activity_participant2: string;
  activity_participant3: string;
  activity_participant4: string;
  activity_participant5: string;
}

