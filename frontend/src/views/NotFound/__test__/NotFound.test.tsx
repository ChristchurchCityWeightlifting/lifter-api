/** @format */

import React from "react";
import { test, expect } from "@jest/globals";
import renderer from "react-test-renderer";
import NotFound from "../NotFound";

test("Not Found renders correctly", () => {
  const tree = renderer.create(<NotFound />).toJSON();

  expect(tree).toMatchSnapshot();
});