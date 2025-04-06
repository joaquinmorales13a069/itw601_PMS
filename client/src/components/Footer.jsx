import React from 'react'

export default function Footer() {
  return (
    <footer className="bg-[#3FA37F] text-white">
        <div className="max-w-7xl mx-auto px-4 py-3 text-center">
          <p className="text-sm">
            &copy; {new Date().getFullYear()} Patient Management System. All rights reserved.
          </p>
        </div>
      </footer>
  )
}
