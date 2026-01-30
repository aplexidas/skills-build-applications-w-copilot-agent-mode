import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts API Endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="text-center">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-2">Loading workouts...</p>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="alert alert-danger" role="alert">
        <strong>Error!</strong> {error}
      </div>
    </div>
  );

  return (
    <div className="container mt-4">
      <h2><i className="bi bi-dumbbell"></i> Workout Suggestions</h2>
      <div className="row">
        {workouts.length === 0 ? (
          <div className="col-12">
            <p className="text-center">No workouts found</p>
          </div>
        ) : (
          workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">{workout.name}</h5>
                  <p className="card-text">{workout.description}</p>
                  <ul className="list-group list-group-flush">
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <span><strong>Type:</strong> {workout.workout_type}</span>
                      <span className="badge bg-primary rounded-pill">{workout.workout_type}</span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <span><strong>Duration:</strong></span>
                      <span className="badge bg-info rounded-pill">{workout.duration} min</span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <span><strong>Difficulty:</strong></span>
                      <span className={`badge rounded-pill ${workout.difficulty_level === 'Hard' ? 'bg-danger' : workout.difficulty_level === 'Medium' ? 'bg-warning' : 'bg-success'}`}>
                        {workout.difficulty_level}
                      </span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <span><strong>Calories:</strong></span>
                      <span className="badge bg-secondary rounded-pill">{workout.estimated_calories} kcal</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Workouts;
