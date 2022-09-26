/** @format */

import React from "react";
import { Typography } from "@mui/material";

interface TitleProps {
  children?: React.ReactNode;
}

const Title: React.FC<React.PropsWithChildren<TitleProps>> = (
  props: TitleProps
) => {
  return (
    <Typography color="primary" variant="h2" gutterBottom {...props}>
      {props.children}
    </Typography>
  );
};

export default Title;
