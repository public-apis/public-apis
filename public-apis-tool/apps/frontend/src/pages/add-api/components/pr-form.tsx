import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Switch } from "@/components/ui/switch";
import React, { useState } from "react";

const PRForm = () => {
  const [category, setCategory] = useState("");
  const [name, setName] = useState("");
  const [link, setLink] = useState("");
  const [description, setDescription] = useState("");
  const [auth, setAuth] = useState("No");
  const [https, setHttps] = useState(false);
  const [cors, setCors] = useState("Unknown");
  const [postmanLink, setPostmanLink] = useState("");

  const authValues = ["No", "OAuth", "apiKey", "X-Mashape-Key", "User-Agent"];
  const corsValues = ["Unknown", "No", "Yes"];

  return (
    <div className="flex w-full items-center justify-center px-2">
      <div className="flex flex-col w-full gap-3 max-w-132">
        <div className="flex flex-col">
          <label htmlFor="name" className="opacity-75 px-2">
            API Name
          </label>
          <input
            name="name"
            id="name"
            type="text"
            className="bg-zinc-100 dark:bg-zinc-800 rounded-md p-2 outline-0"
            value={name}
            onChange={(e) => {
              setName(e.target.value);
            }}
          />
        </div>
        <div className="flex flex-col">
          <label htmlFor="link" className="opacity-75 px-2">
            API Link
          </label>
          <input
            name="link"
            id="link"
            type="text"
            className="bg-zinc-100 dark:bg-zinc-800 rounded-md p-2 outline-0"
            value={link}
            onChange={(e) => {
              setLink(e.target.value);
            }}
          />
        </div>
        <div className="flex flex-col">
          <label htmlFor="description" className="opacity-75 px-2">
            Description
          </label>
          <textarea
            maxLength={100}
            name="description"
            id="description"
            className="bg-zinc-100 dark:bg-zinc-800 rounded-md p-2 outline-0 resize-none"
            value={description}
            onChange={(e) => {
              setDescription(e.target.value);
            }}
          ></textarea>
        </div>
        <div className="flex flex-col">
          <label className="opacity-75 px-2">Auth</label>
          <Select
            defaultValue={authValues[0]}
            value={auth}
            onValueChange={(val) => {
              setAuth(val);
            }}
          >
            <SelectTrigger className="w-full outline-0 border-0 bg-zinc-800 text-md p-2">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              {authValues.map((val) => (
                <SelectItem key={val} value={val}>
                  {val}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <div className="flex flex-col gap-2 px-2">
          <label className="opacity-75">HTTPS</label>
          <Switch checked={https} onCheckedChange={setHttps} />
        </div>

        <div className="flex flex-col">
          <label className="opacity-75 px-2">CORS</label>
          <Select
            defaultValue={corsValues[0]}
            value={cors}
            onValueChange={(val) => {
              setCors(val);
            }}
          >
            <SelectTrigger className="w-full outline-0 border-0 bg-zinc-800 text-md p-2">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              {corsValues.map((val) => (
                <SelectItem key={val} value={val}>
                  {val}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>
        <div className="flex flex-col">
          <label htmlFor="postman" className="opacity-75 px-2">
            Postman Link (optional)
          </label>
          <input
            name="postman"
            id="postman"
            type="text"
            className="bg-zinc-100 dark:bg-zinc-800 rounded-md p-2 outline-0"
            value={postmanLink}
            onChange={(e) => {
              setPostmanLink(e.target.value);
            }}
          />
        </div>
        <button className="bg-blue-700 text-zinc-100 w-full text-center p-2 shadow-blue-700/30 hover:bg-blue-600 hover:shadow-lg rounded-lg cursor-pointer transition-all duration-300">
          Add API
        </button>
      </div>
    </div>
  );
};

export default PRForm;
