# File: app.py

import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os
import csv

# Define constants
NUM_JOBS = 1000
REGIONS = ["North America", "Europe", "Asia", "South America", "Africa", "Australia"]
CITIES = {
    "North America": ["New York", "San Francisco", "Toronto", "Chicago", "Seattle", "Austin"],
    "Europe": ["London", "Berlin", "Paris", "Amsterdam", "Madrid", "Dublin"],
    "Asia": ["Singapore", "Tokyo", "Bangalore", "Shanghai", "Seoul", "Dubai"],
    "South America": ["Sao Paulo", "Buenos Aires", "Bogota", "Lima", "Santiago"],
    "Africa": ["Cape Town", "Nairobi", "Lagos", "Cairo", "Johannesburg"],
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"]
}

# Career clusters and associated jobs
CAREER_CLUSTERS = {
    "Technology": [
        "Software Engineer", "Data Scientist", "UI/UX Designer", "DevOps Engineer",
        "Cloud Architect", "Machine Learning Engineer", "Mobile Developer", "Cybersecurity Analyst"
    ],
    "Business": [
        "Business Analyst", "Marketing Manager", "Financial Analyst", "Project Manager",
        "Product Manager", "Operations Manager", "Management Consultant", "Human Resources Manager"
    ],
    "Healthcare": [
        "Registered Nurse", "Physician", "Physical Therapist", "Medical Technologist",
        "Pharmacist", "Healthcare Administrator", "Biomedical Engineer", "Medical Researcher"
    ],
    "Creative Arts": [
        "Graphic Designer", "Content Creator", "Digital Artist", "Video Editor",
        "Game Developer", "Audio Engineer", "Animator", "Creative Director"
    ],
    "Education": [
        "Teacher", "Educational Consultant", "Curriculum Developer", "School Counselor",
        "Education Technology Specialist", "Special Education Teacher", "Academic Advisor", "Instructional Designer"
    ],
    "Science & Research": [
        "Research Scientist", "Environmental Scientist", "Laboratory Technician", "Biologist",
        "Chemist", "Physicist", "Materials Scientist", "Astrophysicist"
    ]
}

# Skills required for different job categories
TECHNICAL_SKILLS = {
    "Technology": [
        "Python", "JavaScript", "Java", "SQL", "React", "AWS", "Docker", "Machine Learning",
        "C++", "Git", "Kubernetes", "Node.js", "TensorFlow", "PyTorch", "CI/CD", "Cloud Computing"
    ],
    "Business": [
        "Microsoft Excel", "Data Analysis", "Project Management", "Marketing", "Financial Modeling",
        "CRM Software", "SQL", "Business Intelligence", "Tableau", "PowerBI", "Google Analytics", "Budgeting"
    ],
    "Healthcare": [
        "Patient Care", "Medical Terminology", "Electronic Health Records", "Clinical Assessment",
        "Medical Software", "Laboratory Techniques", "Healthcare Regulations", "Biology", "Chemistry"
    ],
    "Creative Arts": [
        "Adobe Creative Suite", "Photoshop", "Illustrator", "After Effects", "Blender", "Unity",
        "Unreal Engine", "3D Modeling", "Color Theory", "Typography", "UI/UX", "Sketch"
    ],
    "Education": [
        "Curriculum Development", "Educational Technology", "Classroom Management",
        "Instructional Design", "Assessment", "Learning Management Systems", "Online Course Development"
    ],
    "Science & Research": [
        "MATLAB", "R", "Scientific Writing", "Laboratory Techniques", "Data Analysis", "Research Methods",
        "Statistical Analysis", "Experimental Design", "Scientific Instrumentation", "Python"
    ]
}

SOFT_SKILLS = [
    "Communication", "Teamwork", "Problem Solving", "Critical Thinking",
    "Time Management", "Leadership", "Adaptability", "Creativity",
    "Emotional Intelligence", "Conflict Resolution", "Attention to Detail",
    "Self-Motivation", "Work Ethic", "Interpersonal Skills", "Negotiation"
]

PERSONALITY_TRAITS = [
    "Analytical", "Creative", "Detail-oriented", "Outgoing", "Organized",
    "Innovative", "Methodical", "People-oriented", "Task-oriented", "Adaptable",
    "Risk-taker", "Cautious", "Independent", "Collaborative", "Practical", "Visionary"
]

EXPERIENCE_LEVELS = ["Entry-level", "Mid-level", "Senior", "Manager", "Director", "Executive"]
EDUCATION_LEVELS = ["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "PhD", "Certification"]
WORK_ARRANGEMENTS = ["On-site", "Remote", "Hybrid", "Flexible"]
COMPANY_SIZES = ["Startup (1-50)", "Small (51-200)", "Medium (201-1000)", "Large (1000+)", "Enterprise (10000+)"]
INDUSTRY_GROWTH = ["High Growth", "Stable Growth", "Moderate Growth", "Slow Growth", "Emerging Field"]
SALARY_RANGES = {
    "Entry-level": {"min": 40000, "max": 80000},
    "Mid-level": {"min": 70000, "max": 120000},
    "Senior": {"min": 100000, "max": 180000},
    "Manager": {"min": 120000, "max": 200000},
    "Director": {"min": 150000, "max": 250000},
    "Executive": {"min": 200000, "max": 400000}
}

# Get all technical skills for multi-select dropdown
ALL_TECHNICAL_SKILLS = []
for skills in TECHNICAL_SKILLS.values():
    ALL_TECHNICAL_SKILLS.extend(skills)
ALL_TECHNICAL_SKILLS = sorted(list(set(ALL_TECHNICAL_SKILLS)))

# Generate a datetime within the last month
def random_date():
    now = datetime.now()
    days_ago = random.randint(1, 30)
    date = now - timedelta(days=days_ago)
    return date.strftime("%Y-%m-%d")

# Generate job data
def generate_job_postings(num_jobs):
    jobs = []
    job_id = 1

    for _ in range(num_jobs):
        # Select cluster and job title
        cluster = random.choice(list(CAREER_CLUSTERS.keys()))
        job_title = random.choice(CAREER_CLUSTERS[cluster])
        
        # Select experience level and corresponding salary
        experience_level = random.choice(EXPERIENCE_LEVELS)
        salary_range = SALARY_RANGES[experience_level]
        salary = random.randint(salary_range["min"], salary_range["max"])
        
        # Select region and city
        region = random.choice(REGIONS)
        city = random.choice(CITIES[region])
        
        # Select required technical skills (3-6 skills)
        num_tech_skills = random.randint(3, 6)
        if cluster in TECHNICAL_SKILLS:
            technical_skills = random.sample(TECHNICAL_SKILLS[cluster], min(num_tech_skills, len(TECHNICAL_SKILLS[cluster])))
        else:
            technical_skills = []
        
        # Select required soft skills (2-4 skills)
        num_soft_skills = random.randint(2, 4)
        soft_skills = random.sample(SOFT_SKILLS, num_soft_skills)
        
        # Select preferred personality traits (2-3 traits)
        num_personality_traits = random.randint(2, 3)
        personality_traits = random.sample(PERSONALITY_TRAITS, num_personality_traits)
        
        # Other job details
        education_level = random.choice(EDUCATION_LEVELS)
        work_arrangement = random.choice(WORK_ARRANGEMENTS)
        company_size = random.choice(COMPANY_SIZES)
        industry_growth = random.choice(INDUSTRY_GROWTH)
        
        # Job engagement metrics (for popularity/demand)
        applications = random.randint(10, 500)
        views = applications * random.randint(5, 15)
        save_rate = round(random.uniform(0.05, 0.4), 2)  # % of viewers who saved the job
        
        # Create a job posting
        job = {
            "job_id": job_id,
            "title": job_title,
            "career_cluster": cluster,
            "company_name": f"Company {job_id}",  # Simplified company names
            "region": region,
            "city": city,
            "salary": salary,
            "experience_level": experience_level,
            "education_required": education_level,
            "technical_skills": ", ".join(technical_skills),
            "soft_skills": ", ".join(soft_skills),
            "preferred_traits": ", ".join(personality_traits),
            "work_arrangement": work_arrangement,
            "company_size": company_size,
            "industry_growth": industry_growth,
            "posting_date": random_date(),
            "applications_received": applications,
            "job_views": views,
            "save_rate": save_rate,
            "job_description": f"This is a {experience_level} {job_title} position requiring expertise in {', '.join(technical_skills)}. The ideal candidate should have strong {', '.join(soft_skills)} skills and be {', '.join(personality_traits)}."
        }
        
        jobs.append(job)
        job_id += 1
    
    return jobs

# Recommendation function
def recommend_jobs(jobs_df, user_profile):
    """
    Recommendation function
    
    Parameters:
    jobs_df - DataFrame with job postings
    user_profile - Dictionary with user information including:
        - skills: list of user's skills
        - personality: list of personality traits
        - preferred_regions: list of preferred regions
        - experience_level: desired experience level
    
    Returns:
    DataFrame with recommended jobs sorted by relevance score
    """
    # Create a copy of the jobs dataframe
    results = jobs_df.copy()
    
    # Calculate relevance scores
    results['relevance_score'] = 0
    
    # Score based on skills match
    for idx, job in results.iterrows():
        # Technical skills match
        tech_skills = job['technical_skills'].split(', ') if not pd.isna(job['technical_skills']) else []
        skill_match = sum(skill in tech_skills for skill in user_profile['skills'])
        results.at[idx, 'relevance_score'] += skill_match * 3  # Higher weight for technical skills
        
        # Personality match
        personality_traits = job['preferred_traits'].split(', ') if not pd.isna(job['preferred_traits']) else []
        trait_match = sum(trait in personality_traits for trait in user_profile['personality'])
        results.at[idx, 'relevance_score'] += trait_match * 2
        
        # Region match
        if job['region'] in user_profile['preferred_regions']:
            results.at[idx, 'relevance_score'] += 5
            
        # Experience level match
        if job['experience_level'] == user_profile['experience_level']:
            results.at[idx, 'relevance_score'] += 4
    
    # Sort by relevance score
    results = results.sort_values(by='relevance_score', ascending=False)
    
    return results

# Check if CSV exists, if not generate it
def get_job_data():
    csv_file = "career_job_postings.csv"
    if not os.path.exists(csv_file):
        job_postings = generate_job_postings(NUM_JOBS)
        jobs_df = pd.DataFrame(job_postings)
        jobs_df.to_csv(csv_file, index=False)
        return jobs_df
    else:
        return pd.read_csv(csv_file)

# Streamlit app
def main():
    st.set_page_config(
        page_title="AI Career Guidance Platform",
        page_icon="🎓",
        layout="wide"
    )
    
    st.title("🎓 AI Career Guidance Platform")
    st.markdown("### Find your ideal career path based on your skills and preferences")
    
    # Sidebar for user inputs
    st.sidebar.header("Your Profile")
    
    # Load job data 
    jobs_df = get_job_data()
    
    # Use multiselect to get user skills
    user_skills = st.sidebar.multiselect(
        "Select your technical skills:", 
        options=ALL_TECHNICAL_SKILLS,
        help="Choose the technical skills that you possess"
    )
    
    # Personality traits
    user_personality = st.sidebar.multiselect(
        "Select your personality traits:",
        options=PERSONALITY_TRAITS,
        default=["Analytical", "Detail-oriented"],
        help="Choose traits that best describe your work personality"
    )
    
    # Preferred regions
    user_regions = st.sidebar.multiselect(
        "Preferred work regions:",
        options=REGIONS,
        default=["North America"],
        help="Where would you like to work?"
    )
    
    # Experience level
    user_experience = st.sidebar.selectbox(
        "Your experience level:",
        options=EXPERIENCE_LEVELS,
        index=0,
        help="Select your current experience level"
    )
    
    # Search button
    search_button = st.sidebar.button("Find Matching Jobs", type="primary")
    
    # Additional filters
    st.sidebar.markdown("---")
    st.sidebar.header("Additional Filters")
    
    filter_work_arrangement = st.sidebar.multiselect(
        "Work Arrangement:",
        options=WORK_ARRANGEMENTS,
        help="Filter by preferred work arrangement"
    )
    
    min_salary = st.sidebar.slider(
        "Minimum Salary ($):",
        min_value=30000,
        max_value=400000,
        value=50000,
        step=5000,
        help="Filter by minimum salary"
    )
    
    # Show data tab
    tab1, tab2 = st.tabs(["Job Recommendations", "Data Analytics"])
    
    with tab1:
        if search_button:
            if not user_skills:
                st.warning("Please select at least one skill to find matching jobs.")
            else:
                st.success(f"Finding jobs matching your {len(user_skills)} skills and preferences...")
                
                # Create user profile
                user_profile = {
                    "skills": user_skills,
                    "personality": user_personality,
                    "preferred_regions": user_regions,
                    "experience_level": user_experience
                }
                
                # Get recommendations
                recommendations = recommend_jobs(jobs_df, user_profile)
                
                # Apply additional filters if any
                if filter_work_arrangement:
                    recommendations = recommendations[recommendations['work_arrangement'].isin(filter_work_arrangement)]
                
                if min_salary > 30000:
                    recommendations = recommendations[recommendations['salary'] >= min_salary]
                
                # Display results count
                if len(recommendations) > 0:
                    st.markdown(f"### Found {len(recommendations)} matching jobs")
                    
                    # Display job cards
                    for i, (_, job) in enumerate(recommendations.head(10).iterrows()):
                        col1, col2 = st.columns([3, 1])
                        
                        with col1:
                            st.markdown(f"#### {job['title']} at {job['company_name']}")
                            st.markdown(f"**Location:** {job['city']}, {job['region']}")
                            st.markdown(f"**Salary:** ${job['salary']:,}")
                            st.markdown(f"**Required Skills:** {job['technical_skills']}")
                            st.markdown(f"**Experience Level:** {job['experience_level']}")
                            
                        with col2:
                            # Show score and match percentage
                            match_percentage = min(int(job['relevance_score'] * 5), 100)
                            st.markdown(f"### {match_percentage}% Match")
                            
                            # Apply color based on match
                            if match_percentage >= 80:
                                st.markdown("🟢 Strong Match")
                            elif match_percentage >= 50:
                                st.markdown("🟡 Good Match")
                            else:
                                st.markdown("🟠 Fair Match")
                        
                        # Show expandable job description
                        with st.expander("View Job Details"):
                            st.markdown(f"**Education Required:** {job['education_required']}")
                            st.markdown(f"**Soft Skills:** {job['soft_skills']}")
                            st.markdown(f"**Work Arrangement:** {job['work_arrangement']}")
                            st.markdown(f"**Company Size:** {job['company_size']}")
                            st.markdown(f"**Industry Growth:** {job['industry_growth']}")
                            st.markdown(f"**Job Description:**")
                            st.markdown(job['job_description'])
                        
                        st.markdown("---")
                else:
                    st.warning("No jobs match your criteria. Try adjusting your skills or filters.")
        else:
            # Initial state
            st.info("👈 Select your skills and preferences, then click 'Find Matching Jobs'")
            st.image("https://via.placeholder.com/800x400?text=AI+Career+Guidance", use_column_width=True)
    
    with tab2:
        st.header("Career Data Analytics")
        
        # Basic stats about the job market
        st.subheader("Job Market Overview")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Job Postings", f"{len(jobs_df):,}")
        with col2:
            avg_salary = int(jobs_df['salary'].mean())
            st.metric("Average Salary", f"${avg_salary:,}")
        with col3:
            top_cluster = jobs_df['career_cluster'].value_counts().idxmax()
            st.metric("Top Career Cluster", top_cluster)
        
        # Distribution of jobs by career cluster
        st.subheader("Jobs by Career Cluster")
        cluster_counts = jobs_df['career_cluster'].value_counts()
        st.bar_chart(cluster_counts)
        
        # Distribution of jobs by experience level
        st.subheader("Jobs by Experience Level")
        experience_counts = jobs_df['experience_level'].value_counts()
        st.bar_chart(experience_counts)
        
        # Top skills in demand
        st.subheader("Top Skills in Demand")
        
        # Parse skills from all job listings
        all_skills = []
        for skills_str in jobs_df['technical_skills'].dropna():
            all_skills.extend([s.strip() for s in skills_str.split(',')])
        
        skill_counts = pd.Series(all_skills).value_counts().head(10)
        st.bar_chart(skill_counts)

if __name__ == "__main__":
    main()