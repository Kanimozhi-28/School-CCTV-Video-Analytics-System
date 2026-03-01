
def validate_pairing(detected_faces, relationships):
    """
    Validates if students in the frame are with their authorized parents.
    
    detected_faces: list of dicts {'name': face_id, 'role': 'Student'/'Parent'/'Unknown'}
    relationships: dict {student_face_id: parent_face_id}
    
    Returns: 
        status: 'SAFE', 'SUSPICIOUS', or 'STRANGER'
        alerts: list of alert messages
    """
    students = [f for f in detected_faces if f['role'] == 'Student']
    parents = [f for f in detected_faces if f['role'] == 'Parent']
    unknowns = [f for f in detected_faces if f['role'] == 'Unknown']
    
    alerts = []
    
    # 1. Check for Strangers
    if unknowns:
        for u in unknowns:
            alerts.append(f"STRANGER DETECTED: Unknown individual spotted.")
            
    # 2. Check Student Pairings
    for s in students:
        s_id = s['name']
        authorized_parent_id = relationships.get(s_id)
        
        # Is the authorized parent in the same frame?
        is_with_parent = any(p['name'] == authorized_parent_id for p in parents)
        
        if not is_with_parent:
            # If student is alone or with a stranger/wrong parent
            alerts.append(f"SUSPICIOUS: Student {s_id} is not with their authorized guardian.")
            
    # Overall Status
    if any("SUSPICIOUS" in a for a in alerts):
        return "SUSPICIOUS", alerts
    if any("STRANGER" in a for a in alerts):
        return "STRANGER", alerts
        
    return "SAFE", ["All individuals are authorized and paired correctly."]
