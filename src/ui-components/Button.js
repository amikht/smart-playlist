import { Link } from "react-router-dom";

export default function Button(props) {
    return (
    <Link 
        to={props.linkTo}
        className={"font-bold text-white py-2 px-4 rounded bg-" + props.buttonColor + "-400 hover:bg-" + props.buttonColor + "-600 float-right " + props.buttonStyle}>
            {props.buttonText}
    </Link>
    );
}