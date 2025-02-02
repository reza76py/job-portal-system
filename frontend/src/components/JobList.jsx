import React, { useEffect, useState } from "react";
import axios from "axios";

const JobList = () => {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/jobs")
      .then(response => {
        setJobs(response.data);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>Available Jobs</h2>
      <ul>
        {jobs.map(job => (
          <li key={job.id}>
            <h3>{job.title}</h3>
            <p>{job.description}</p>
            <button onClick={() => window.location.href=`/apply/${job.id}`}>Apply</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default JobList;
