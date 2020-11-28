import React from "react";
import { Switch, Redirect, Route } from "react-router-dom";

import { Home } from "../pages/Home";
import { Reviewpage } from "../pages/Review";

function Router() {
  return (
    <Switch>
      <Route exact path="/" render={() => <Home></Home>} />
      <Route path="/review" render={() => <Reviewpage></Reviewpage>} />
      <Redirect path="*" to="/" />
    </Switch>
  );
}

export default Router;
