import React, { useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

const ApplyJob = () => {
  const { jobId } = useParams();
  const [coverLetter, setCoverLetter] = useState("");

  const handleSubmit = () => {
    axios.post(`http://127.0.0.1:8000/api/jobs/apply/${jobId}/`, { cover_letter: coverLetter })
      .then(response => alert("Application submitted!"))
      .catch(error => console.error(error));
  };

  return (
    <div>
      <h2>Apply for Job</h2>
      <textarea value={coverLetter} onChange={(e) => setCoverLetter(e.target.value)} placeholder="Write your cover letter..." />
      <button onClick={handleSubmit}>Submit Application</button>
    </div>
  );
};

export default ApplyJob;
