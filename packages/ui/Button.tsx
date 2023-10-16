import * as React from "react";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: any;
}

export const Button = ({ children, ...rest }: ButtonProps) => {
  return <button {...rest}>{children}</button>;
};
