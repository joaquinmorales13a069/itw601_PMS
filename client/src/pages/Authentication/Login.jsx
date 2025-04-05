// Login.jsx
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {
    FaEnvelope,
    FaLock,
    FaEye,
    FaEyeSlash,
    FaFacebookF,
    FaTwitter,
    FaGoogle,
} from "react-icons/fa";
import AuthLayout from "../../components/layouts/AuthLayout";
import axiosInstance from "../../utils/axiosInstance";
import { API_PATHS } from "../../utils/apiPaths";

// import images
import AuthImage from "../../assets/images/PMS_1.jpg";
import { validateEmail } from "../../utils/helper";

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    // const [rememberMe, setRememberMe] = useState(false);
    const [showPassword, setShowPassword] = useState(false);
    const [error, setError] = useState(null);

    // navigate import
    const navigate = useNavigate();

    // Auto-fill email if remembered
    useEffect(() => {
        const rememberedEmail = localStorage.getItem("rememberedEmail");
        if (rememberedEmail) {
            setEmail(rememberedEmail);
        }
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();

        // Check for a valid email address
        if (!validateEmail(email)) {
            setError("Please enter a valid email address");
            return;
        }
        // Check for a password
        if (!password) {
            setError("Please enter your password");
            return;
        }

        // API LOGIC
        try {
            const response = await axiosInstance.post(API_PATHS.AUTH.LOGIN, {
                email,
                password,
            });

            const { token, user } = response.data;

            if (token) {
                localStorage.setItem("token", token);
                navigate("/");
            }
        } catch (error) {
            if (error.response && error.response.data.message) {
                setError(error.response.data.message);
            } else {
                setError("Something went wrong. Please try again");
            }
        }
    };

    const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
    };

    return (
        <AuthLayout>
            <div className="flex flex-col md:flex-row bg-white p-5 rounded-xl shadow-md w-full max-w-[800px]">
                {/* Image Section */}
                <div className="flex-1 text-center p-5">
                    <h2 className="text-xl font-bold bg-[#004d40] text-white p-2 rounded-md mb-4">
                        Patient Management System
                    </h2>
                    {/* TODO: Add Medical Staff image here */}
                    <img
                        src={AuthImage}
                        alt="Medical Staff"
                        className="max-w-full rounded-md mx-auto"
                    />
                </div>
                {/* Login Section */}
                <div className="flex-1 p-5">
                    <h2 className="text-2xl font-bold mb-3">Sign in</h2>
                    <p className="mb-4">
                        If you don’t have an account,{" "}
                        <a
                            href="/register"
                            className="text-red-500 font-bold no-underline"
                        >
                            Register here!
                        </a>
                    </p>
                    <form onSubmit={handleSubmit}>
                        <label
                            htmlFor="email"
                            className="block mb-1 font-medium"
                        >
                            Email
                        </label>
                        <div className="flex items-center border-b-2 border-black my-2 p-1">
                            <FaEnvelope className="mr-2 text-gray-600" />
                            <input
                                type="email"
                                id="email"
                                placeholder="Enter your email address"
                                required
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                className="flex-grow border-none outline-none p-1"
                            />
                        </div>
                        <label
                            htmlFor="password"
                            className="block mb-1 font-medium"
                        >
                            Password
                        </label>
                        <div className="flex items-center border-b-2 border-black my-2 p-1 relative">
                            <FaLock className="mr-2 text-gray-600" />

                            <input
                                type={showPassword ? "text" : "password"}
                                id="password"
                                placeholder="Enter your password"
                                required
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                className="flex-grow border-none outline-none p-1"
                            />

                            <div
                                className="cursor-pointer"
                                onClick={togglePasswordVisibility}
                            >
                                {showPassword ? <FaEyeSlash /> : <FaEye />}
                            </div>
                            {/*error handling*/}
                            {error && (
                                <p className={" text-red-500 text-xs pb-2.5"}>
                                    {error}
                                </p>
                            )}
                        </div>
                        {/* <div className="flex justify-between text-sm my-2">
                            <label className="flex items-center">
                                <input
                                    type="checkbox"
                                    id="rememberMe"
                                    checked={rememberMe}
                                    onChange={(e) =>
                                        setRememberMe(e.target.checked)
                                    }
                                    className="mr-1"
                                />
                                Remember me
                            </label>
                            <a
                                href="#"
                                className="text-blue-500 hover:underline"
                            >
                                Forgot Password?
                            </a>
                        </div> */}
                        <button
                            type="submit"
                            className="w-full p-3 bg-red-500 text-white rounded-md cursor-pointer text-lg"
                        >
                            Login
                        </button>
                    </form>
                    <div className="flex justify-center my-3">
                        or continue with
                    </div>
                    <div className="flex justify-center mt-2 space-x-4">
                        <div className="cursor-pointer">
                            <FaFacebookF className="text-2xl" />
                        </div>
                        <div className="cursor-pointer">
                            <FaTwitter className="text-2xl" />
                        </div>
                        <div className="cursor-pointer">
                            <FaGoogle className="text-2xl" />
                        </div>
                    </div>
                </div>
            </div>
        </AuthLayout>
    );
};

export default Login;
