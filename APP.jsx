
import React, { useState, useEffect } from 'react';

const App = () => {

    const [data, setData] = useState(null);

    useEffect(() => {

        fetch('http://127.0.0.1:8000/')
            .then(response => response.json())
            .then(json => setData(json))
            .catch(error => console.error("Error:", error));

    }, []);

    return (
        <div>
            <h1>React + FastAPI</h1>

            {data ? (
                <h2>{data.message}</h2>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default App;


