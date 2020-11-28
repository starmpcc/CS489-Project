import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";

export function Home() {
  const [message, setMessage] = useState("loading...");

  fetch("http://localhost:3001/api")
    .then((res) => res.json())
    .then((data) => setMessage(data.title));

  useEffect(() => {
    console.log("message...?", message);
  }, [message]);

  return (
    <div>
      <h1>{message}</h1>
    </div>
  );
}
