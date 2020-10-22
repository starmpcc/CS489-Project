import React from "react";
import { BrowserRouter } from "react-router-dom";
import { Topbar } from "./components/Topbar";
import Router from "./router/Router";

function App() {
  return (
    <BrowserRouter>
      <Topbar></Topbar>
      <Router></Router>
    </BrowserRouter>
  );
}

export default App;
