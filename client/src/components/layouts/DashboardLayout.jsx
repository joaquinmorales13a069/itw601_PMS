import React from "react";
import Navbar from "../Navbar";
import Footer from "../Footer";
import { FaStar } from "react-icons/fa";

export default function DashboardLayout({ children, patientName }) {
    return (
        <div className="flex flex-col min-h-screen font-sans bg-gray-100 text-gray-800">
            {/* Navbar */}
            <Navbar />

            {/* Main Content */}
            <div className="flex flex-grow">
                {/* Sidebar */}
                <aside className="w-1/4 bg-white shadow-md p-4">
                    <div className="flex items-center mb-6">
                        <div className="w-12 h-12 bg-gray-300 rounded-full flex items-center justify-center">
                            <FaStar className="text-[#3FA37F] text-xl" />
                        </div>
                        <div className="ml-4">
                            <h3 className="text-lg font-bold">
                                {patientName || "Patient.name"}
                            </h3>
                        </div>
                    </div>

                    <nav className="space-y-4">
                        <button className="w-full text-left p-3 bg-[#3FA37F] text-white rounded-md">
                            Patient Information
                        </button>
                        <button className="w-full text-left p-3 bg-[#3FA37F] text-white rounded-md">
                            Appointment
                        </button>
                        <button className="w-full text-left p-3 bg-[#3FA37F] text-white rounded-md">
                            Medical Records
                        </button>
                    </nav>
                </aside>

                {/* Main Content Area */}
                <main className="flex-grow bg-gray-50 p-6">{children}</main>
            </div>

            {/* Footer */}
            <Footer />
        </div>
    );
}
