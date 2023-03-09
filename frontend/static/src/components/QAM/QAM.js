import { useNavigate } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "../../Auth/AuthContextProvider";
import "./QAM.css"

function QAM(props) {
    const navigate = useNavigate()
    const {isAuth, logout} = useContext(AuthContext)
	return (
		<div id="QAM">
			<h1>Quick access Menu</h1>
            <nav id="main-nav">
                <button onClick={() => logout()} >My Profile</button>
                <button onClick={() => (navigate("/home"))} >Home</button>
                <button onClick={() => (navigate("/weather"))} >Weather</button>
                <button onClick={() => (navigate("/entities"))} >Celestial Lookup</button>
            </nav>
            {isAuth 
                    ?
                    <button onClick={() => logout()} >Sign out</button>
                    :
                    <nav id="footer-nav">
                        <button onClick={() => (navigate("/login"))} >Login</button> 
                        <button onClick={() => (navigate("/register"))} >Sign up</button>
                    </nav>   
            }
		</div>
	);
}

export default QAM;
