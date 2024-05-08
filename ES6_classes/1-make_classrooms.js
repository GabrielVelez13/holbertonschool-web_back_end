import ClassRoom from "./0-classroom.js";

export default function initializeRooms() {
  const nineteen = new ClassRoom(19);
  const twenty = new ClassRoom(20);
  const thirtyfour = new ClassRoom(34);

  return [nineteen, twenty, thirtyfour];
}