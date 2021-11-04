import Button from "./Button";

export default function MenuBar(...props) {
    return (
        <div className="flex flex-row container mx-auto max-w-screen-2xl bg-gray-200 px-3 py-4">
            <Button buttonText="Smart Playlists!" buttonColor="gray" linkTo="/" buttonStyle={"flex-none"}/>
            <div className="flex relative container max-w-7xl justify-end font-sans font-light">
                <Button buttonText="Login" buttonColor="blue" linkTo="/login"/>
                <Button buttonText="Register" buttonColor="green" linkTo="/register"/>
            </div>
        </div>
    );
}