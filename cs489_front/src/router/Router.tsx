import React from "react";
import { Switch, Redirect, Route } from "react-router-dom";

import { Home } from "../pages/Home";

function Router(props: { isTop: boolean }) {
  return (
    <Switch>
      <Route exact path="/" render={() => <Home isTop={props.isTop}></Home>} />
      <Redirect path="*" to="/" />
    </Switch>
  );
}

export default Router;
