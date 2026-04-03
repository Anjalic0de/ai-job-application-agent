from langgraph.graph import StateGraph

def fetch_job(state):
    print("Fetching job:", state["job_url"])
    return state

def generate_resume(state):
    print("Tailoring resume...")
    return state

def generate_cover_letter(state):
    print("Generating cover letter...")
    return state

def detect_ats(state):
    url = state["job_url"]

    if "workday" in url:
        state["ats"] = "Workday"
    elif "greenhouse" in url:
        state["ats"] = "Greenhouse"
    elif "lever" in url:
        state["ats"] = "Lever"
    else:
        state["ats"] = "Unknown"

    print("Detected ATS:", state["ats"])
    return state

from utils.browser import open_and_fill_form

def submit_application(state):
    print("Starting browser automation...")

    try:
        open_and_fill_form(state["job_url"], state)
        state["status"] = "success"
    except Exception as e:
        print("Error during submission:", e)
        state["status"] = "failed"
        state["failure_reason"] = str(e)

    # Logging (important for assignment)
    if "ats" not in state or state["ats"] == "Unknown":
        state["failure_reason"] = "ATS not detected"

    print("Application attempt done")
    return state

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("fetch_job", fetch_job)
    graph.add_node("resume", generate_resume)
    graph.add_node("cover_letter", generate_cover_letter)
    graph.add_node("detect_ats", detect_ats)
    graph.add_node("submit", submit_application)

    graph.set_entry_point("fetch_job")

    graph.add_edge("fetch_job", "resume")
    graph.add_edge("resume", "cover_letter")
    graph.add_edge("cover_letter", "detect_ats")
    graph.add_edge("detect_ats", "submit")

    return graph.compile()