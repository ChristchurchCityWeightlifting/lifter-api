/** @format */

import LiftObjectProps from "../../interfaces";

export interface LiftTableProps {
  liftSet: LiftObjectProps[];
}

export interface WeightCategoryTableProps {
  lifts: LiftObjectProps[];
}
export interface WeightCategoryCollapsableRowProps {
  weightCategory: string;
  groupByWeightCategory: groupByWeightCategoryProps;
}

export interface groupByWeightCategoryProps {
  [key: string]: LiftObjectProps[];
}
