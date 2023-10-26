import { InputField } from "@/app/components/InputField";
import React from "react";

const Signup = () => {
  return (
    <div className="max-w-5xl mx-auto flex items-center justify-center">
      <div className="max-w-sm flex flex-1 flex-col bg-white p-8">
        <h3 className="font-extrabold text-md text-center p-5">Sign up</h3>
        <InputField
          label="Email"
          type="email"
          placeholder="enter email"
          htmlFor="signup_email"
        />
        <InputField
          label="Password"
          type="password"
          placeholder="enter password"
          htmlFor="signup_password"
        />
        <InputField
          label="Confirm password"
          type="password"
          placeholder="reenter password"
          htmlFor="signup_confirm_password"
        />

        <button
          className="bg-gray-700 hover:bg-gray-800 font-semibold text-sm text-white rounded-md p-2"
          type="button"
        >
          Login
        </button>
      </div>
    </div>
  );
};

export default Signup;
