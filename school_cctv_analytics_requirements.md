# School CCTV Video Analytics System - Requirements Document

## 1. System Overview
An intelligent live screen read - CCTV video analytics system for school premises that identifies individuals, validates their authorization status, and detects suspicious activities by analyzing student-parent pairings in real-time.

## 2. Core Objectives
- **Enhance School Security**: Detect and alert on unauthorized individuals entering school premises
- **Validate Relationships**: Ensure students leave with authorized guardians only
- **Immediate Response**: Enable rapid security team response through instant WhatsApp alerts

## 3. Functional Requirements

### 3.1 Face Recognition Database
- Maintain a comprehensive database containing:
  - **Student faces**: All enrolled students with multiple angle captures
  - **Parent/Guardian faces**: Authorized pickup persons linked to respective students
  - **Staff faces**: Teachers, administrators, and authorized personnel
- Support for multiple guardians per student (parents, grandparents, authorized relatives)
- Regular database updates for new admissions and changes

### 3.2 Stranger Detection
- **Real-time monitoring** of all CCTV feeds across school premises
- **Automatic identification** of faces not present in the authorized database
- **Alert triggering** when unknown individuals are detected in:
  - School entrance/exit points
  - Corridors and common areas
  - Near classrooms during school hours
  - Playground and parking areas

### 3.3 Student-Guardian Pairing Validation
- **Authorized Pair Detection**: Recognize when a student is with their registered parent/guardian
  - System marks as "SAFE" - no alert required
  - Log the interaction for audit purposes
  
- **Suspicious Pair Detection**: Identify when a student is with an unrecognized adult
  - Flag as "SUSPICIOUS" immediately
  - Trigger instant alert with snapshot and location
  - Continue tracking until resolved

### 3.4 Alert System
- **WhatsApp Integration** for instant notifications to:
  - School security team
  - Principal/Administrator on duty
  - Designated emergency response personnel
  
- **Alert Content** must include:
  - Timestamp and location (camera ID/zone)
  - Snapshot of the detected person/pair
  - Alert type: "STRANGER DETECTED" or "SUSPICIOUS PAIRING"
  - Severity level: High/Medium based on location and context

## 4. Technical Requirements

### 4.1 Video Analytics Engine
- Multi-camera feed processing capability (minimum 10-20 cameras)
- Real-time face detection and recognition (processing delay < 3 seconds)
- High accuracy rate (>95% recognition accuracy in good lighting)
- Handle varying lighting conditions, angles, and partial occlusions

### 4.2 Database Management
- Scalable database supporting 500-2000+ face profiles
- Quick search and match capability (<2 seconds per match)
- Secure storage with encrypted face data
- Easy interface for adding/updating/removing profiles

### 4.3 Integration Points
- **CCTV System**: Compatible with existing IP camera infrastructure
- **WhatsApp Business API**: For reliable alert delivery
- **Admin Dashboard**: Web-based interface for monitoring and configuration

## 5. Key Use Cases

### Use Case 1: Unknown Person Entry
**Scenario**: A person without an authorized face profile enters school premises  
**System Action**: Detect face → Search database → No match found → Send WhatsApp alert with photo and location → Security responds

### Use Case 2: Safe Student Pickup
**Scenario**: Parent arrives to pick up their child after school  
**System Action**: Detect both faces → Match student-parent pair → Validate relationship → Log as authorized pickup → No alert

### Use Case 3: Suspicious Pairing
**Scenario**: Student seen with an unregistered adult near exit gate  
**System Action**: Detect pairing → Student match found → Adult no match → Flag as suspicious → Immediate WhatsApp alert → Track movement → Security intervenes

## 6. Non-Functional Requirements

### 6.1 Performance
- 24/7 system availability during school operational hours
- Minimal false positive rate (<5%)
- Alert delivery within 5 seconds of detection

### 6.2 Security & Privacy
- Encrypted face data storage (GDPR/data protection compliant)
- Access controls for system administration
- Audit logs for all alerts and database changes
- Parental consent for face data collection

### 6.3 Scalability
- Support for expanding to multiple school campuses
- Ability to add more cameras without performance degradation
- Database growth accommodation (yearly enrollment increases)

## 7. Success Metrics
- **Detection Accuracy**: >95% successful identification rate
- **Response Time**: Alerts delivered within 5 seconds
- **False Positive Rate**: <5% of total alerts
- **System Uptime**: >99% during operational hours
- **Security Incidents Prevented**: Measurable reduction in unauthorized access

## 8. Implementation Priorities
1. **Phase 1**: Deploy at main entrance/exit with stranger detection
2. **Phase 2**: Add student-parent pairing validation at pickup zones
3. **Phase 3**: Expand to full campus coverage with all zones monitored
4. **Phase 4**: Advanced analytics (behavior pattern detection, crowd monitoring)

---

**Document Version**: 1.0  
**Date**: December 2025  
**Status**: Draft for Review
