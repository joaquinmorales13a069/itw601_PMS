import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import {
    FaEnvelope,
    FaLock,
    FaEye,
    FaEyeSlash,
    FaUser,
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

const SignUp = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [name, setName] = useState("");
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);
    const [error, setError] = useState(null);

    // navigate import
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        // Form validation
        if (!name) {
            setError("Please enter your name");
            return;
        }

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

        // Check password length
        if (password.length < 6) {
            setError("Password must be at least 6 characters long");
            return;
        }

        // Check passwords match
        if (password !== confirmPassword) {
            setError("Passwords do not match");
            return;
        }

        // API LOGIC
        try {
            const response = await axiosInstance.post(API_PATHS.AUTH.REGISTER, {
                email,
                password,
                name,
                // Role is automatically set to patient on the server
            });

            const { token, user } = response.data;

            if (token) {
                localStorage.setItem("token", token);
                navigate("/patient/dashboard");
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

    const toggleConfirmPasswordVisibility = () => {
        setShowConfirmPassword(!showConfirmPassword);
    };

    return (
        <AuthLayout>
            <div className="flex flex-col md:flex-row bg-white p-5 rounded-xl shadow-md w-full max-w-[800px]">
                {/* Image Section */}
                <div className="flex-1 text-center p-5">
                    <h2 className="text-xl font-bold bg-[#004d40] text-white p-2 rounded-md mb-4">
                        Patient Management System
                    </h2>
                    <img
                        src={AuthImage}
                        alt="Medical Staff"
                        className="max-w-full rounded-md mx-auto"
                    />
                </div>
                {/* SignUp Section */}
                <div className="flex-1 p-5">
                    <h2 className="text-2xl font-bold mb-3">Sign Up</h2>
                    <p className="mb-4">
                        Already have an account?{" "}
                        <Link to={'/login'} className="text-red-500 font-bold no-underline">
                            Login here!
                        </Link>
                    </p>
                    <form onSubmit={handleSubmit}>
                        <label
                            htmlFor="name"
                            className="block mb-1 font-medium"
                        >
                            Full Name
                        </label>
                        <div className="flex items-center border-b-2 border-black my-2 p-1">
                            <FaUser className="mr-2 text-gray-600" />
                            <input
                                type="text"
                                id="name"
                                placeholder="Enter your full name"
                                required
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                                className="flex-grow border-none outline-none p-1"
                            />
                        </div>

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
                        </div>

                        <label
                            htmlFor="confirmPassword"
                            className="block mb-1 font-medium"
                        >
                            Confirm Password
                        </label>
                        <div className="flex items-center border-b-2 border-black my-2 p-1 relative">
                            <FaLock className="mr-2 text-gray-600" />
                            <input
                                type={showConfirmPassword ? "text" : "password"}
                                id="confirmPassword"
                                placeholder="Confirm your password"
                                required
                                value={confirmPassword}
                                onChange={(e) => setConfirmPassword(e.target.value)}
                                className="flex-grow border-none outline-none p-1"
                            />
                            <div
                                className="cursor-pointer"
                                onClick={toggleConfirmPasswordVisibility}
                            >
                                {showConfirmPassword ? <FaEyeSlash /> : <FaEye />}
                            </div>
                        </div>

                        {/* Error message */}
                        {error && (
                            <p className="text-red-500 text-xs mt-2 mb-2">
                                {error}
                            </p>
                        )}

                        <button
                            type="submit"
                            className="w-full p-3 bg-red-500 text-white rounded-md cursor-pointer text-lg mt-4"
                        >
                            Sign Up
                        </button>
                    </form>
                    <div className="flex justify-center my-3">
                        or sign up with
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

export default SignUp;
