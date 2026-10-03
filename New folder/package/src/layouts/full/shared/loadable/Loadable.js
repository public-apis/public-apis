import React, { Suspense } from "react";

const Loadable = (Component) => (props) =>
(
  <Suspense>
    <Component {...props} />
  </Suspense>
);

export default Loadable;
