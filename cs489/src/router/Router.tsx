import React from "react";
import { Switch, Redirect, Route } from "react-router-dom";

import { Home } from "../pages/Home";
import { Reviewpage } from "../pages/Review";
import { Testpage } from "../pages/TestPage";
import { Reviewtable } from "../pages/ReviewTable";
import { Functionintro } from "../pages/FunctionIntro";
import { Teamintro } from "../pages/TeamIntro";

function Router() {
  return (
    <Switch>
      <Route exact path="/" render={() => <Home></Home>} />
      <Route path="/test" render={() => <Testpage></Testpage>} />
      <Route path="/review" render={() => <Reviewpage></Reviewpage>} />
      <Route path="/table" render={() => <Reviewtable></Reviewtable>} />
      <Route path="/team" render={() => <Teamintro></Teamintro>} />
      <Route path="/function" render={() => <Functionintro></Functionintro>} />
      <Redirect path="*" to="/" />
    </Switch>
  );
}

export default Router;
