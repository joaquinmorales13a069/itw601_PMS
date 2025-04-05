import React from 'react'
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate
} from "react-router-dom"
import Home from './pages/Home/Home'
import Login from './pages/Authentication/Login'
import SignUp from './pages/Authentication/SignUp'


export default function App() {
  return (
    <div>
		<Router>
			<Routes>
				{/* Add all project routes using react-router-dom */}
				<Route path='/' element={<Home />} />
				<Route path='/login' element={<Login />}/>
				<Route path='/signup' element={<SignUp />}/>
			</Routes>
		</Router>
    </div>
  )
}
