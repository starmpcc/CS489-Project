import React from "react";
import { BrowserRouter } from "react-router-dom";
import { Topbar } from "./components/Topbar";

function App() {
  return (
    <BrowserRouter>
      <Topbar></Topbar>
    </BrowserRouter>
  );
}

export default App;
