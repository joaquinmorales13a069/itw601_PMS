// AuthLayout.jsx
import React, { useState } from 'react';
import { FiMenu, FiX } from 'react-icons/fi';

function AuthLayout({ children }) {
  const [menuOpen, setMenuOpen] = useState(false);

  const handleMenuToggle = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <div className="flex flex-col min-h-screen font-sans bg-white text-gray-800">
      {/* NAVBAR */}
      <nav className="bg-[#3FA37F] text-white">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex justify-between items-center py-4">
            {/* Brand / Logo */}
            <div className="text-xl font-bold">
              Patient Management System
            </div>

            {/* Desktop Menu */}
            <div className="hidden md:flex space-x-6">
              <a href="#" className="hover:text-gray-100 transition-colors">
                Home
              </a>
              <a href="#" className="hover:text-gray-100 transition-colors">
                About
              </a>
              <a href="#" className="hover:text-gray-100 transition-colors">
                Contact
              </a>
            </div>

            {/* Mobile Menu Button */}
            <button
              type="button"
              className="md:hidden focus:outline-none"
              onClick={handleMenuToggle}
            >
              {menuOpen ? <FiX size={24} /> : <FiMenu size={24} />}
            </button>
          </div>

          {/* Mobile Menu Dropdown */}
          {menuOpen && (
            <div className="flex flex-col md:hidden pb-4 space-y-2">
              <a href="#" className="hover:text-gray-100 transition-colors">
                Home
              </a>
              <a href="#" className="hover:text-gray-100 transition-colors">
                About
              </a>
              <a href="#" className="hover:text-gray-100 transition-colors">
                Contact
              </a>
            </div>
          )}
        </div>
      </nav>

      {/* MAIN CONTENT (children = SignUp.jsx or other auth forms) */}
      <main className="flex-grow flex justify-center items-center p-4">
        {children}
      </main>

      {/* FOOTER */}
      <footer className="bg-[#3FA37F] text-white">
        <div className="max-w-7xl mx-auto px-4 py-3 text-center">
          <p className="text-sm">
            &copy; {new Date().getFullYear()} Patient Management System. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}

export default AuthLayout;