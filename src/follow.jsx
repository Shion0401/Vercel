import React from "react";
import axios from "axios";

function App() {
    const [data, setData] = React.useState();
    const url = " https://stormy-wildwood-55177-3fddc74bdc1b.herokuapp.com";

    const GetData = () => {
        axios.get(url).then((res) => {
            setData(res.data);
        });
    };
    return (
        <div>
            <div>ここに処理を書いていきますよその２</div>
            {data ? <div>{data.Hello}</div> : <button onClick={GetData}>てすと</button>}
        </div>
    );
}

export default App;