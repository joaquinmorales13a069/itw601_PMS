// AuthLayout.jsx
import React from 'react';
import Navbar from '../Navbar';
import Footer from '../Footer';

function AuthLayout({ children }) {

  return (
    <div className="flex flex-col min-h-screen font-sans bg-white text-gray-800">
      {/* Navbar */}
      <Navbar />

      {/* MAIN CONTENT (children = SignUp.jsx or other auth forms) */}
      <main className="flex-grow flex justify-center items-center p-4">
        {children}
      </main>

      {/* FOOTER */}
      <Footer />
    </div>
  );
}

export default AuthLayout;